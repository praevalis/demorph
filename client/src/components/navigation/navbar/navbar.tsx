import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { RxCross1, RxHamburgerMenu } from 'react-icons/rx';

import type { CtaData } from '@/types/ui';
import type { NavLink } from '@/types/navigation';

import { Button } from '@/components/ui/button';
import logo from '@/assets/images/demorph-logo.png';

export default function Navbar() {
	const [nav, setNav] = useState(false);

	const { t } = useTranslation();
	const links = t('navbar.links', { returnObjects: true }) as NavLink[];
	const navLinks = Array.isArray(links) ? links : [];

	const ctaData = t('navbar.cta', { returnObjects: true }) as CtaData;

	return (
		<nav className='absolute flex items-center justify-between w-full px-4 md:px-8 py-5 lg:w-[80vw] mx-auto z-50'>
			<Link to='/' onClick={() => setNav(false)}>
				<div className='inline-flex gap-3 items-center hover:opacity-90 transition-opacity'>
					<img
						src={logo}
						alt='Demorph Logo'
						className='max-w-none rounded-md  h-14 w-14 object-contain'
					/>
					<h3 className='text-2xl text-white font-primary'>DEMORPH</h3>
				</div>
			</Link>

			<div className='inline-flex items-center gap-4'>
				{/* Desktop Menu */}
				<ul className='hidden md:flex flex-row gap-5 px-4 py-3 bg-black text-white text-xs font-secondary rounded-md'>
					{navLinks.map((link) => (
						<li key={link.href}>
							<Link
								to={link.href}
								className='hover:text-gray-300 transition-colors'
							>
								{link.label}
							</Link>
						</li>
					))}
				</ul>

				<Button asChild className='hidden md:flex'>
					<Link to={ctaData.href}>{ctaData.label}</Link>
				</Button>

				{/* Mobile Hamburger Button */}
				<button
					onClick={() => setNav(!nav)}
					className='-translate-y-1 p-2 text-white bg-black rounded-xl md:hidden focus:outline-none focus:ring-2 focus:ring-gray-500'
					aria-label={nav ? 'Close menu' : 'Open menu'}
					aria-expanded={nav}
				>
					{nav ? (
						<RxCross1 className='w-5 h-5' />
					) : (
						<RxHamburgerMenu className='w-5 h-5' />
					)}
				</button>
			</div>

			{/* Mobile Menu Dropdown */}
			{nav && (
				<div className='absolute left-0 right-0 top-full px-2 pt-2 md:hidden'>
					<ul className='flex flex-col gap-5 p-4 text-xs text-white bg-black border border-gray-800 rounded-md shadow-xl font-secondary'>
						{navLinks.map((link) => (
							<li key={link.href}>
								<Link
									to={link.href}
									onClick={() => setNav(false)}
									className='block w-full py-1 hover:text-gray-300'
								>
									{link.label}
								</Link>
							</li>
						))}

						<li className='pt-2 border-t border-gray-800'>
							<Button asChild className='w-full' onClick={() => setNav(false)}>
								<Link to={ctaData.href}>{ctaData.label}</Link>
							</Button>
						</li>
					</ul>
				</div>
			)}

			{/* Backdrop to close mobile nav when clicked outside the menu. */}
			{nav && (
				<div
					className='fixed inset-0 z-[-1] bg-transparent'
					onClick={() => setNav(false)}
				/>
			)}
		</nav>
	);
}
