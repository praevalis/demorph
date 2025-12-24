export interface CtaData {
	label: string;
	href: string;
}

export interface AboutCardData {
	icon: string;
	layout: 'horizontal' | 'vertical';
	heading: string;
	text: string;
}

export interface FeatureCardData {
	text: string;
}

export interface BenefitPointData {
	icon: string;
	label: string;
	description: string;
}
