import Hero from '@/features/home/hero';
import About from '@/features/home/about';
import Feature from '@/features/home/feature';
import Benefit from '@/features/home/benefit';
import Algorithm from '@/features/home/algorithm';
import BlogBanner from '@/features/home/blog-banner';
import DefaultLayout from '@/components/layout/default-layout';

export default function Home() {
	return (
		<DefaultLayout>
			<Hero />
			<About />
			<Feature />
			<BlogBanner />
			<Algorithm />
			<Benefit />
		</DefaultLayout>
	);
}
