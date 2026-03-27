import { Wifi, Coffee, Music, Wind } from 'lucide-react';

export function About() {
  return (
    <section id="about" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
        <div className="grid grid-cols-2 gap-4">
          <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=2070&auto=format&fit=crop" className="rounded-2xl w-full h-64 object-cover hover:opacity-90 transition-opacity" alt="Spa Interior" />
          <img src="https://images.unsplash.com/photo-1620733723572-11c52f7c2d82?q=80&w=2070&auto=format&fit=crop" className="rounded-2xl w-full h-64 object-cover mt-8 hover:opacity-90 transition-opacity" alt="Spa Details" />
        </div>
        <div className="space-y-8">
          <h2 className="text-4xl font-medium text-stone-900 tracking-tight">A Sanctuary of <br /><span className="font-serif italic text-stone-500">Quiet Luxury</span></h2>
          <div className="space-y-6 text-stone-600 font-light leading-relaxed">
            <p>Designed with minimalism and nature in mind, Calm & Cozy Spa features 8 private treatment suites, each equipped with the latest Japanese Takara Belmont spa beds.</p>
            <p>Every detail, from the ambient lighting to the curated playlist and aromatherapy scents, is chosen to transport you away from the city noise into a state of deep zen.</p>
          </div>
          <div className="grid grid-cols-2 gap-6 pt-4 border-t border-stone-100">
            <div className="flex items-center gap-3">
              <Wifi className="w-5 h-5 text-[#2C2420]" />
              <span className="text-sm font-medium">Digital Detox Zone</span>
            </div>
            <div className="flex items-center gap-3">
              <Coffee className="w-5 h-5 text-[#2C2420]" />
              <span className="text-sm font-medium">Tea Lounge</span>
            </div>
            <div className="flex items-center gap-3">
              <Music className="w-5 h-5 text-[#2C2420]" />
              <span className="text-sm font-medium">Binaural Beats</span>
            </div>
            <div className="flex items-center gap-3">
              <Wind className="w-5 h-5 text-[#2C2420]" />
              <span className="text-sm font-medium">Air Purification</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
