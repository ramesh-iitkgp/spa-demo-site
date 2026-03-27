import { Sparkles, ArrowDown, PlayCircle, Droplets, Waves, Leaf, UserCheck } from 'lucide-react';

export function Hero() {
  return (
    <header className="relative min-h-screen flex items-center overflow-hidden">
      {/* Background Image with Parallax effect */}
      <div className="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1540555700478-4be289fbecef?q=80&w=2070&auto=format&fit=crop" alt="Spa Interior" className="w-full h-full object-cover opacity-90 scale-105" />
        <div className="absolute inset-0 bg-gradient-to-r from-stone-900/80 via-stone-900/40 to-transparent"></div>
        <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-5 mix-blend-overlay"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-6 w-full pt-20 pb-32">
        <div className="max-w-3xl space-y-8 fade-up">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white/90 text-[10px] uppercase tracking-[0.2em] font-medium shadow-sm">
            <Sparkles className="w-3 h-3 text-amber-200" />
            Voted #1 Head Spa in Los Angeles
          </div>
          
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-medium text-white tracking-tighter leading-[0.95]">
            Awaken Your <br />
            <span className="font-serif italic text-stone-200">Inner Harmony</span>
          </h1>
          
          <p className="text-lg md:text-xl text-stone-200/90 font-light leading-relaxed max-w-xl border-l-2 border-white/30 pl-6 fade-up delay-100">
            Experience the viral Korean Head Spa therapy. A dedicated sanctuary for scalp detoxification, deep relaxation, and holistic renewal using premium organic botanicals.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-5 pt-6 fade-up delay-200">
            <button className="bg-white text-[#2C2420] px-8 py-4 rounded-full text-xs uppercase tracking-widest font-bold hover:bg-stone-100 transition-all shadow-xl hover:shadow-2xl flex items-center justify-center gap-3 group">
              View Service Menu
              <ArrowDown className="w-4 h-4 group-hover:translate-y-1 transition-transform" />
            </button>
            <button className="bg-transparent border border-white/40 text-white px-8 py-4 rounded-full text-xs uppercase tracking-widest font-bold hover:bg-white/10 transition-colors backdrop-blur-sm flex items-center justify-center gap-3">
              <PlayCircle className="w-4 h-4" />
              Watch The Experience
            </button>
          </div>
        </div>

        {/* Quick Features */}
        <div className="absolute bottom-0 left-0 right-0 border-t border-white/10 bg-black/20 backdrop-blur-md">
          <div className="max-w-7xl mx-auto px-6 py-6 grid grid-cols-2 md:grid-cols-4 gap-8">
            <div className="flex items-center gap-3 text-white/80">
              <Droplets className="w-5 h-5 opacity-70" />
              <span className="text-xs uppercase tracking-wider font-medium">Scalp Detox</span>
            </div>
            <div className="flex items-center gap-3 text-white/80">
              <Waves className="w-5 h-5 opacity-70" />
              <span className="text-xs uppercase tracking-wider font-medium">Water Therapy</span>
            </div>
            <div className="flex items-center gap-3 text-white/80">
              <Leaf className="w-5 h-5 opacity-70" />
              <span className="text-xs uppercase tracking-wider font-medium">Organic Ampoules</span>
            </div>
            <div className="flex items-center gap-3 text-white/80">
              <UserCheck className="w-5 h-5 opacity-70" />
              <span className="text-xs uppercase tracking-wider font-medium">Private Suites</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
