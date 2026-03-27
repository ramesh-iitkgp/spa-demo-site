import { Microscope, Sparkles, Moon } from 'lucide-react';

export function Benefits() {
  return (
    <section id="benefits" className="py-24 bg-white relative">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid lg:grid-cols-2 gap-16 items-center mb-20">
          <div className="space-y-6">
            <span className="text-[#2C2420] text-xs font-bold tracking-widest uppercase flex items-center gap-2">
              <span className="w-8 h-[1px] bg-[#2C2420]"></span>
              Why Korean Head Spa?
            </span>
            <h2 className="text-4xl md:text-5xl font-medium text-stone-900 tracking-tight leading-tight">
              More than just a <br /><span className="font-serif italic text-stone-500">deep cleanse.</span>
            </h2>
            <p className="text-stone-600 leading-relaxed font-light text-lg">
              Our specialized head spa treatments go beyond traditional hair care. We combine trichology-based scalp analysis with therapeutic massage to address the root causes of hair loss, stress, and fatigue.
            </p>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="aspect-square bg-stone-100 rounded-2xl overflow-hidden relative group">
              <img src="https://images.unsplash.com/photo-1519823551278-64ac927accc9?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Scalp Health" />
              <div className="absolute bottom-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1.5 rounded-lg text-xs font-medium">Scalp Health</div>
            </div>
            <div className="aspect-square bg-stone-100 rounded-2xl overflow-hidden relative group translate-y-8">
              <img src="https://images.unsplash.com/photo-1600334129128-685c5582fd35?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Relaxation" />
              <div className="absolute bottom-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1.5 rounded-lg text-xs font-medium">Relaxation</div>
            </div>
          </div>
        </div>

        {/* Benefit Cards */}
        <div className="grid md:grid-cols-3 gap-8">
          <div className="p-8 bg-stone-50 rounded-2xl border border-stone-100 hover:border-[#2C2420]/20 transition-colors group">
            <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center text-[#2C2420] mb-6 group-hover:scale-110 transition-transform">
              <Microscope className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-stone-900 mb-3">Micro-Camera Analysis</h3>
            <p className="text-sm text-stone-600 leading-relaxed">We visualize your scalp's condition before and after treatment to target oil buildup, dead skin, and sensitivity.</p>
          </div>
          <div className="p-8 bg-stone-50 rounded-2xl border border-stone-100 hover:border-[#2C2420]/20 transition-colors group">
            <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center text-[#2C2420] mb-6 group-hover:scale-110 transition-transform">
              <Sparkles className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-stone-900 mb-3">Deep Purification</h3>
            <p className="text-sm text-stone-600 leading-relaxed">Remove product buildup and unclog follicles to promote healthier, faster hair growth and volume.</p>
          </div>
          <div className="p-8 bg-stone-50 rounded-2xl border border-stone-100 hover:border-[#2C2420]/20 transition-colors group">
            <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center text-[#2C2420] mb-6 group-hover:scale-110 transition-transform">
              <Moon className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-stone-900 mb-3">Stress Reduction</h3>
            <p className="text-sm text-stone-600 leading-relaxed">Targeted acupressure on the head, neck, and shoulders relieves tension headaches and improves sleep quality.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
