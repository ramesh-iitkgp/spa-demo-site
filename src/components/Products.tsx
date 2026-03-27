import { Leaf, Flower, Droplet, Sun } from 'lucide-react';

export function Products() {
  return (
    <section className="py-16 border-y border-stone-200 bg-white">
      <div className="max-w-7xl mx-auto px-6 text-center">
        <p className="text-stone-400 text-xs font-bold tracking-[0.2em] uppercase mb-8">Premium Organic Botanicals</p>
        <div className="flex flex-wrap justify-center gap-12 md:gap-20 opacity-60 grayscale hover:grayscale-0 transition-all duration-500">
          <div className="text-2xl font-serif font-bold text-stone-800 flex items-center gap-2"><Leaf className="w-6 h-6" /> AROMATICA</div>
          <div className="text-2xl font-serif font-bold text-stone-800 flex items-center gap-2"><Flower className="w-6 h-6" /> INNISFREE</div>
          <div className="text-2xl font-serif font-bold text-stone-800 flex items-center gap-2"><Droplet className="w-6 h-6" /> SULWHASOO</div>
          <div className="text-2xl font-serif font-bold text-stone-800 flex items-center gap-2"><Sun className="w-6 h-6" /> RYO</div>
        </div>
      </div>
    </section>
  );
}
