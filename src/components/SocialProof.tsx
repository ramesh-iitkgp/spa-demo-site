import { Instagram } from 'lucide-react';

export function SocialProof() {
  return (
    <section className="py-24 bg-stone-50 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 mb-12 flex justify-between items-end">
        <div>
          <span className="text-[#2C2420] text-xs font-bold tracking-widest uppercase mb-2 block">@CalmAndCozySpa</span>
          <h2 className="text-3xl font-medium text-stone-900">Follow Our Journey</h2>
        </div>
        <button className="hidden md:flex items-center gap-2 text-sm font-bold border-b border-stone-300 pb-1 hover:border-[#2C2420] transition-colors">
          <Instagram className="w-4 h-4" /> Follow Us
        </button>
      </div>
      
      <div className="grid grid-cols-2 md:grid-cols-5 gap-1">
        <div className="relative group aspect-square overflow-hidden bg-stone-200">
          <img src="https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Instagram Post" />
          <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <Instagram className="w-6 h-6 text-white" />
          </div>
        </div>
        <div className="relative group aspect-square overflow-hidden bg-stone-200">
          <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Instagram Post" />
          <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <Instagram className="w-6 h-6 text-white" />
          </div>
        </div>
        <div className="relative group aspect-square overflow-hidden bg-stone-200 hidden md:block">
          <img src="https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Instagram Post" />
          <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <Instagram className="w-6 h-6 text-white" />
          </div>
        </div>
        <div className="relative group aspect-square overflow-hidden bg-stone-200 hidden md:block">
          <img src="https://images.unsplash.com/photo-1522337660859-02fbefca4702?q=80&w=2069&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Instagram Post" />
          <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <Instagram className="w-6 h-6 text-white" />
          </div>
        </div>
        <div className="relative group aspect-square overflow-hidden bg-stone-200">
          <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=2070&auto=format&fit=crop" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Instagram Post" />
          <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
            <Instagram className="w-6 h-6 text-white" />
          </div>
        </div>
      </div>
    </section>
  );
}
