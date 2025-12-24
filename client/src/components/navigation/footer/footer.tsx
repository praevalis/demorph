import { Link } from 'react-router-dom';
import { FiGithub } from 'react-icons/fi';
import { Trans, useTranslation } from 'react-i18next';
import { FaXTwitter, FaLinkedinIn } from 'react-icons/fa6';

import type { SocialLink } from '@/types/navigation';

import { Button } from '@/components/ui/button';
import logo from '@/assets/images/demorph-logo.png';

export default function Footer() {
	const { t } = useTranslation();
	const socialLinks = t('footer.socials', {
		returnObjects: true,
	}) as SocialLink[];

	const iconClass = 'w-5 h-5 md:w-6 md:h-6 transition-all';
	const socialIconMap: Record<string, React.ReactNode> = {
		linkedin: <FaLinkedinIn className={iconClass} />,
		twitter: <FaXTwitter className={iconClass} />,
		github: <FiGithub className={iconClass} />,
	};

	return (
		<footer className='w-full px-4 md:px-[12vw] pt-14 md:pt-24 pb-14 bg-black'>
			<div className='flex flex-col md:flex-row md:justify-between gap-6'>
				<div className='flex flex-col gap-10'>
					<Link to='/'>
						<div className='inline-flex gap-3 items-center hover:opacity-90 transition-opacity'>
							<img
								src={logo}
								alt='Demorph Logo'
								className='max-w-none rounded-md h-14 w-14 object-contain'
							/>
							<h3 className='text-2xl text-white font-primary'>DEMORPH</h3>
						</div>
					</Link>
					<p className='hidden md:block max-w-md text-sm text-white/70 font-poppins'>
						{t('footer.message')}
					</p>
				</div>
				<div className='flex flex-col gap-6 md:gap-14'>
					<div className='flex gap-2'>
						{socialLinks.map((social, idx) => (
							<Button
								asChild
								key={idx}
								intent='gray'
								shape='social'
								className=''
							>
								<a href={social.href} target='_blank' rel='noreferrer'>
									{socialIconMap[social.icon] || (
										<FiGithub className={iconClass} />
									)}
								</a>
							</Button>
						))}
					</div>
					<p className='text-sm text-white/70 font-poppins'>
						<Trans
							i18nKey='footer.copyright'
							components={[
								<a
									href='https://akshatdmishra.com'
									target='_blank'
									rel='noreferrer'
									className='hover:underline font-medium text-secondary'
									key='0'
								/>,
							]}
						/>
					</p>
					<p className='md:hidden text-sm text-white/70 font-poppins'>
						{t('footer.message')}
					</p>
				</div>
			</div>
		</footer>
	);
}
