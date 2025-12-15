from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.core.metadata import ApiTags
from src.user.services import UserService
from src.user.dependencies import get_user_service
from src.auth.dependencies import get_current_user
from src.core.exceptions.exceptions import Forbidden
from src.user.dtos import UserDto, UserInternalDto, UserCreateDto, UserUpdateDto

router = APIRouter(prefix='/users', tags=[ApiTags.user])


@router.get(
    '/me',
    status_code=status.HTTP_200_OK,
    response_model=UserDto,
    response_model_by_alias=True,
)
async def get_current_user_controller(
    current_user: UserInternalDto = Depends(get_current_user),
) -> UserDto:
    """
    Controller to get user.

    Args:
        current_user: Authenticated user.

    Returns:
        UserDto: Fetched user.
    """
    return UserDto.model_validate(current_user)


@router.get(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=UserDto,
    response_model_by_alias=True,
)
async def get_user_controller(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
    _: UserInternalDto = Depends(get_current_user),
) -> UserDto:
    """
    Controller to get user.

    Args:
        user_id: ID of the user to fetch.
        user_service: Injected user service.

    Returns:
        UserDto: Fetched user.
    """
    internal_user = await user_service.get_user(user_id)
    return UserDto.model_validate(internal_user)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=UserDto,
    response_model_by_alias=True,
)
async def create_user_controller(
    create_dto: UserCreateDto, user_service: UserService = Depends(get_user_service)
) -> UserDto:
    """
    Controller to create user.

    Args:
        create_dto: Data to create user.
        user_service: Injected user service.

    Returns:
        UserDto: Created user.
    """
    return await user_service.create_user(create_dto)


@router.patch(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=UserDto,
    response_model_by_alias=True,
)
async def update_user_controller(
    user_id: UUID,
    update_dto: UserUpdateDto,
    user_service: UserService = Depends(get_user_service),
    current_user: UserInternalDto = Depends(get_current_user),
) -> UserDto:
    """
    Controller to update user.

    Args:
        user_id: ID of the user to update.
        update_dto: Data used for update.
        user_service: Injected user service.
        current_user: Authenticated user.

    Returns:
        UserDto: Updated user.

    Raises:
    """
    if current_user.id != user_id:
        raise Forbidden('Identity mismatch.')

    return await user_service.update_user(user_id, update_dto)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_controller(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
    current_user: UserInternalDto = Depends(get_current_user),
) -> None:
    """
    Controller to delete an user.

    Args:
        user_id: ID of the user to delete.
        user_service: Injected user service.
        current_user: Authenticated user.
    """
    if current_user.id != user_id:
        raise Forbidden('Identity mismatch.')

    return await user_service.delete_user(user_id)
