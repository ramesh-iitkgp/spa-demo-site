import { Flower2, Phone, ArrowRight } from 'lucide-react';

export function Navigation() {
  return (
    <nav className="sticky top-0 z-40 bg-[#FDFCFB]/80 backdrop-blur-md border-b border-stone-200/60 transition-all duration-300">
      <div className="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
        {/* Logo */}
        <a href="#" className="flex items-center gap-3 group">
          <div className="w-10 h-10 bg-[#2C2420] text-white flex items-center justify-center rounded-full shadow-lg group-hover:scale-105 transition-transform duration-300">
            <Flower2 className="w-5 h-5" />
          </div>
          <div>
            <span className="block text-lg font-bold tracking-tight text-[#2C2420] leading-none">Calm & Cozy</span>
            <span className="text-[10px] uppercase tracking-[0.2em] text-stone-500">Wellness Spa</span>
          </div>
        </a>

        {/* Desktop Links */}
        <div className="hidden lg:flex items-center gap-8 text-[11px] font-semibold uppercase tracking-widest text-stone-500">
          <a href="#about" className="hover:text-[#2C2420] transition-colors py-2">The Sanctuary</a>
          <a href="#benefits" className="hover:text-[#2C2420] transition-colors py-2">Benefits</a>
          <a href="#menu" className="hover:text-[#2C2420] transition-colors py-2">Menu</a>
          <a href="#process" className="hover:text-[#2C2420] transition-colors py-2">The Ritual</a>
          <a href="#team" className="hover:text-[#2C2420] transition-colors py-2">Experts</a>
          <a href="#reviews" className="hover:text-[#2C2420] transition-colors py-2">Stories</a>
        </div>

        {/* CTA */}
        <div className="flex items-center gap-4">
          <a href="tel:+15551234567" className="hidden sm:flex items-center gap-2 text-[#2C2420] font-medium text-xs hover:opacity-70 transition-opacity">
            <Phone className="w-3.5 h-3.5" />
            (555) 123-4567
          </a>
          <button className="bg-[#2C2420] text-white px-6 py-2.5 rounded-full text-[11px] font-semibold uppercase tracking-widest hover:bg-stone-800 transition-all shadow-md hover:shadow-lg active:scale-95 flex items-center gap-2">
            Book Appointment
            <ArrowRight className="w-3 h-3" />
          </button>
        </div>
      </div>
    </nav>
  );
}
