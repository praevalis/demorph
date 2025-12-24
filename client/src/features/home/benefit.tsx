import { useTranslation } from 'react-i18next';
import { GiBullseye } from 'react-icons/gi';
import { MdOutlineElectricBolt } from 'react-icons/md';
import { FaBalanceScaleRight } from 'react-icons/fa';

import type { BenefitPointData } from '@/types/ui';
import { Section } from '@/components/ui/section';

export default function Benefit() {
	const { t } = useTranslation();
	const points = t('benefit.points', {
		returnObjects: true,
	}) as BenefitPointData[];

	const iconMap: Record<string, React.ReactNode> = {
		target: <GiBullseye size={24} />,
		zap: <MdOutlineElectricBolt size={24} />,
		gavel: <FaBalanceScaleRight size={24} />,
	};

	return (
		<Section
			id='benefit'
			className='px-0 md:px-[5vw] lg:px-[5vw] pb-20 bg-background'
		>
			<div className='flex flex-col gap-8 w-full px-4 py-14 md:p-16 font-poppins bg-gradient-to-tr from-dark-gray via-dark-gray to-primary-light rounded-2xl'>
				<div className='flex flex-col gap-4'>
					<h3 className='text-3xl text-white font-semibold'>
						{t('benefit.heading')}
					</h3>
					<p className='max-w-lg text-white/60'>{t('benefit.subheading')}</p>
				</div>
				<div className='grid grid-cols-1 md:grid-cols-3 gap-8'>
					{points.map((point, idx) => (
						<div key={idx} className='flex items-start md:flex-col gap-4'>
							<div className='translate-y-1 shrink-0 p-2 text-white bg-primary-light rounded-xl'>
								{iconMap[point.icon] || <FaBalanceScaleRight size={24} />}
							</div>
							<div className='flex flex-col gap-1'>
								<h5 className='font-bold text-white'>{point.label}</h5>
								<p className='text-white/60'>{point.description}</p>
							</div>
						</div>
					))}
				</div>
			</div>
		</Section>
	);
}
