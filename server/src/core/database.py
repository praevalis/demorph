import contextlib
from typing import TypeVar, AsyncIterator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    AsyncConnection,
    async_sessionmaker,
    create_async_engine,
)


class Base(DeclarativeBase):
    pass


ModelType = TypeVar('ModelType', bound=Base)  # type: ignore


class DatabaseSessionManager:
    def __init__(self) -> None:
        """
        Constructor for database session manager.

        Returns:
            None
        """
        self._engine: AsyncEngine | None = None
        self._sessionmaker: async_sessionmaker | None = None

    def init(self, db_url: str) -> None:
        """
        Initializes engine and sessionmaker for database.

        Args:
            db_url: Connection string for database.

        Returns:
            None
        """
        self._engine = create_async_engine(db_url)
        self._sessionmaker = async_sessionmaker(
            autocommit=False, bind=self._engine, expire_on_commit=False
        )

    async def close(self) -> None:
        """
        Closes the database session manager and cleans up properties.

        Returns:
            None
        """
        if not self._engine:
            raise Exception('Database session manager not initialized.')

        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        """
        Creates a connection object for database.

        Yields:
            AsyncConnection: Connection object.

        Raises:
            Exception: When an error occurs during the connection.
        """
        if not self._engine:
            raise Exception('Database session manager not initialized.')

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

        # Connection is closed by the engine itself.
        # Thus, no need to handle that.

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """
        Creates a session object for database.

        Returns:
            AsyncSession: Session object.

        Raises:
            Exception: When an error occurs during the session.
        """
        if not self._sessionmaker:
            raise Exception('Database session manager not initialized.')

        session = self._sessionmaker()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    # methods to be used for testing
    async def create_all(self, connection: AsyncConnection) -> None:
        """
        Creates all tables attached to a declarative base.

        Args:
            connection: Database connection.

        Returns:
            None
        """
        global Base
        await connection.run_sync(Base.metadata.create_all)

    async def drop_all(self, connection: AsyncConnection) -> None:
        """
        Drops all tables attached to a declarative base.

        Args:
            connection: Database connection.

        Returns:
            None
        """
        global Base
        await connection.run_sync(Base.metadata.drop_all)


sessionmanager = DatabaseSessionManager()
