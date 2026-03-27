/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { AnnouncementBar } from './components/AnnouncementBar';
import { Navigation } from './components/Navigation';
import { Hero } from './components/Hero';
import { Benefits } from './components/Benefits';
import { Process } from './components/Process';
import { Menu } from './components/Menu';
import { Products } from './components/Products';
import { Team } from './components/Team';
import { About } from './components/About';
import { SocialProof } from './components/SocialProof';
import { FAQ } from './components/FAQ';
import { Footer } from './components/Footer';
import { FloatingButton } from './components/FloatingButton';

export default function App() {
  return (
    <div className="bg-[#FDFCFB] text-stone-600 antialiased selection:bg-[#2C2420] selection:text-white">
      <AnnouncementBar />
      <Navigation />
      <Hero />
      <Benefits />
      <Process />
      <Menu />
      <Products />
      <Team />
      <About />
      <SocialProof />
      <FAQ />
      <Footer />
      <FloatingButton />
    </div>
  );
}

