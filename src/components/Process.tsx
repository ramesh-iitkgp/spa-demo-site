import { ScanEye, SprayCan, CloudRain, Waves, Droplet } from 'lucide-react';

export function Process() {
  return (
    <section id="process" className="py-24 bg-[#2C2420] text-stone-300 relative overflow-hidden">
      {/* Abstract Bg Elements */}
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-white/5 rounded-full blur-3xl pointer-events-none -translate-y-1/2 translate-x-1/2"></div>
      
      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="text-center max-w-3xl mx-auto mb-20 space-y-4">
          <span className="text-amber-500/80 text-xs font-bold tracking-widest uppercase">The Process</span>
          <h2 className="text-3xl md:text-4xl font-medium text-white tracking-tight">The 5-Step Restoration Ritual</h2>
          <p className="font-light text-stone-400">A journey designed to reset your scalp's ecosystem.</p>
        </div>

        <div className="relative">
          {/* Connecting Line (Desktop) */}
          <div className="hidden md:block absolute top-12 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
          
          <div className="grid grid-cols-1 md:grid-cols-5 gap-8">
            {/* Step 1 */}
            <div className="relative group text-center md:text-left">
              <div className="w-24 h-24 mx-auto md:mx-0 bg-[#3a312c] rounded-full border border-white/10 flex items-center justify-center mb-6 relative z-10 group-hover:border-amber-500/50 transition-colors">
                <ScanEye className="w-8 h-8 text-white group-hover:text-amber-200 transition-colors" />
                <div className="absolute -top-2 -right-2 w-8 h-8 bg-amber-900 rounded-full flex items-center justify-center text-white text-xs font-bold border border-[#2C2420]">1</div>
              </div>
              <h3 className="text-lg font-medium text-white mb-2">Diagnosis</h3>
              <p className="text-sm text-stone-400 leading-relaxed">Microscopic analysis to identify scalp type and issues.</p>
            </div>

            {/* Step 2 */}
            <div className="relative group text-center md:text-left">
              <div className="w-24 h-24 mx-auto md:mx-0 bg-[#3a312c] rounded-full border border-white/10 flex items-center justify-center mb-6 relative z-10 group-hover:border-amber-500/50 transition-colors">
                <SprayCan className="w-8 h-8 text-white group-hover:text-amber-200 transition-colors" />
                <div className="absolute -top-2 -right-2 w-8 h-8 bg-amber-900 rounded-full flex items-center justify-center text-white text-xs font-bold border border-[#2C2420]">2</div>
              </div>
              <h3 className="text-lg font-medium text-white mb-2">Scaling</h3>
              <p className="text-sm text-stone-400 leading-relaxed">Organic scaling gel application to dissolve impurities.</p>
            </div>

            {/* Step 3 */}
            <div className="relative group text-center md:text-left">
              <div className="w-24 h-24 mx-auto md:mx-0 bg-[#3a312c] rounded-full border border-white/10 flex items-center justify-center mb-6 relative z-10 group-hover:border-amber-500/50 transition-colors">
                <CloudRain className="w-8 h-8 text-white group-hover:text-amber-200 transition-colors" />
                <div className="absolute -top-2 -right-2 w-8 h-8 bg-amber-900 rounded-full flex items-center justify-center text-white text-xs font-bold border border-[#2C2420]">3</div>
              </div>
              <h3 className="text-lg font-medium text-white mb-2">Mist & Steam</h3>
              <p className="text-sm text-stone-400 leading-relaxed">Warm ozone steam opens pores for deep penetration.</p>
            </div>

            {/* Step 4 */}
            <div className="relative group text-center md:text-left">
              <div className="w-24 h-24 mx-auto md:mx-0 bg-[#3a312c] rounded-full border border-white/10 flex items-center justify-center mb-6 relative z-10 group-hover:border-amber-500/50 transition-colors">
                <Waves className="w-8 h-8 text-white group-hover:text-amber-200 transition-colors" />
                <div className="absolute -top-2 -right-2 w-8 h-8 bg-amber-900 rounded-full flex items-center justify-center text-white text-xs font-bold border border-[#2C2420]">4</div>
              </div>
              <h3 className="text-lg font-medium text-white mb-2">Waterfall</h3>
              <p className="text-sm text-stone-400 leading-relaxed">Signature "Yume" head bath and acupressure massage.</p>
            </div>

            {/* Step 5 */}
            <div className="relative group text-center md:text-left">
              <div className="w-24 h-24 mx-auto md:mx-0 bg-[#3a312c] rounded-full border border-white/10 flex items-center justify-center mb-6 relative z-10 group-hover:border-amber-500/50 transition-colors">
                <Droplet className="w-8 h-8 text-white group-hover:text-amber-200 transition-colors" />
                <div className="absolute -top-2 -right-2 w-8 h-8 bg-amber-900 rounded-full flex items-center justify-center text-white text-xs font-bold border border-[#2C2420]">5</div>
              </div>
              <h3 className="text-lg font-medium text-white mb-2">Nourish</h3>
              <p className="text-sm text-stone-400 leading-relaxed">Custom ampoule infusion via galvanic current.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
