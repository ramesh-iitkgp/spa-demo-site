import { Check, Star, PlusCircle } from 'lucide-react';

export function Menu() {
  return (
    <section id="menu" className="py-24 max-w-7xl mx-auto px-6">
      {/* Section Header */}
      <div className="flex flex-col md:flex-row justify-between items-end gap-6 mb-16 border-b border-stone-200 pb-8">
        <div>
          <span className="text-[#2C2420] text-xs font-bold tracking-widest uppercase block mb-3">Service Menu</span>
          <h2 className="text-4xl font-medium text-stone-900 tracking-tight">Curated Treatments</h2>
        </div>
        <div className="flex gap-3">
          <span className="px-4 py-2 rounded-full border border-stone-200 text-xs font-semibold uppercase tracking-wider bg-[#2C2420] text-white">Head Spa</span>
          <span className="px-4 py-2 rounded-full border border-stone-200 text-xs font-semibold uppercase tracking-wider text-stone-500 hover:bg-stone-100 cursor-pointer">Bodywork</span>
          <span className="px-4 py-2 rounded-full border border-stone-200 text-xs font-semibold uppercase tracking-wider text-stone-500 hover:bg-stone-100 cursor-pointer">Add-ons</span>
        </div>
      </div>

      {/* Pricing Cards */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        {/* Card 1 */}
        <div className="bg-white p-8 rounded-[2rem] border border-stone-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative group">
          <div className="mb-6">
            <div className="flex justify-between items-start mb-2">
              <h3 className="text-xl font-bold text-stone-900">The Essential</h3>
              <span className="px-3 py-1 bg-stone-100 rounded-full text-[10px] uppercase font-bold tracking-wide text-stone-600">60 Min</span>
            </div>
            <p className="text-sm text-stone-500">Perfect for first-timers needing a quick refresh.</p>
          </div>
          
          <div className="flex items-baseline gap-1 mb-8">
            <span className="text-4xl font-serif font-medium text-[#2C2420]">$79</span>
          </div>

          <div className="space-y-4 mb-8">
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Scalp Analysis & Diagnosis</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Deep Scaling & Exfoliation</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Basic Scalp Massage</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Shampoo & Conditioning</span>
            </div>
          </div>

          <button className="w-full py-3.5 rounded-xl border border-stone-200 text-stone-900 font-semibold text-xs uppercase tracking-widest hover:bg-[#2C2420] hover:text-white transition-colors">Book Now</button>
        </div>

        {/* Card 2 (Featured) */}
        <div className="bg-[#2C2420] text-white p-8 rounded-[2rem] shadow-2xl relative group transform md:-translate-y-4 border border-[#3E3430]">
          <div className="absolute top-0 right-0 bg-amber-200 text-[#2C2420] text-[10px] font-bold uppercase tracking-widest px-4 py-2 rounded-bl-xl rounded-tr-[2rem]">Most Popular</div>
          
          <div className="mb-6">
            <div className="flex justify-between items-start mb-2">
              <h3 className="text-xl font-bold text-white">The Signature</h3>
              <span className="px-3 py-1 bg-white/10 rounded-full text-[10px] uppercase font-bold tracking-wide text-white/80">90 Min</span>
            </div>
            <p className="text-sm text-stone-400">Deep relaxation with extended massage.</p>
          </div>
          
          <div className="flex items-baseline gap-1 mb-8">
            <span className="text-4xl font-serif font-medium text-white">$119</span>
          </div>

          <div className="space-y-4 mb-8">
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-amber-200" /></div>
              <span className="text-sm text-stone-300"><strong>Everything in Essential</strong></span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-amber-200" /></div>
              <span className="text-sm text-stone-300">Steam Ozone Therapy</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-amber-200" /></div>
              <span className="text-sm text-stone-300"><strong>Waterfall Head Bath</strong></span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-amber-200" /></div>
              <span className="text-sm text-stone-300">Neck & Shoulder Massage (20m)</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-amber-200" /></div>
              <span className="text-sm text-stone-300">Custom Ampoule Injection</span>
            </div>
          </div>

          <button className="w-full py-3.5 rounded-xl bg-white text-[#2C2420] font-bold text-xs uppercase tracking-widest hover:bg-stone-200 transition-colors">Book Signature</button>
        </div>

        {/* Card 3 */}
        <div className="bg-white p-8 rounded-[2rem] border border-stone-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative group">
          <div className="mb-6">
            <div className="flex justify-between items-start mb-2">
              <h3 className="text-xl font-bold text-stone-900">The Royal</h3>
              <span className="px-3 py-1 bg-stone-100 rounded-full text-[10px] uppercase font-bold tracking-wide text-stone-600">120 Min</span>
            </div>
            <p className="text-sm text-stone-500">The ultimate head-to-toe pampering.</p>
          </div>
          
          <div className="flex items-baseline gap-1 mb-8">
            <span className="text-4xl font-serif font-medium text-[#2C2420]">$159</span>
          </div>

          <div className="space-y-4 mb-8">
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600"><strong>Everything in Signature</strong></span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Star className="w-3 h-3 text-amber-500" /></div>
              <span className="text-sm text-stone-600"><strong>Full Facial Treatment</strong></span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Hand & Arm Massage</span>
            </div>
            <div className="flex gap-3 items-start">
              <div className="mt-1 w-5 h-5 rounded-full bg-green-50 flex items-center justify-center shrink-0"><Check className="w-3 h-3 text-green-600" /></div>
              <span className="text-sm text-stone-600">Hot Stone Therapy</span>
            </div>
          </div>

          <button className="w-full py-3.5 rounded-xl border border-stone-200 text-stone-900 font-semibold text-xs uppercase tracking-widest hover:bg-[#2C2420] hover:text-white transition-colors">Book Royal</button>
        </div>

      </div>

      {/* Add On / Bodywork Mini Section */}
      <div className="mt-12 bg-stone-50 rounded-2xl p-8 border border-stone-100">
        <div className="flex items-center gap-2 mb-6">
          <PlusCircle className="w-5 h-5 text-[#2C2420]" />
          <h3 className="font-bold text-stone-900 uppercase tracking-wider text-sm">Popular Add-ons</h3>
        </div>
        <div className="grid md:grid-cols-4 gap-6">
          <div className="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm">
            <span className="text-sm font-medium text-stone-700">Foot Reflexology</span>
            <span className="text-sm font-bold text-[#2C2420]">+$30</span>
          </div>
          <div className="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm">
            <span className="text-sm font-medium text-stone-700">Jelly Mask</span>
            <span className="text-sm font-bold text-[#2C2420]">+$15</span>
          </div>
          <div className="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm">
            <span className="text-sm font-medium text-stone-700">Extra Massage (15m)</span>
            <span className="text-sm font-bold text-[#2C2420]">+$20</span>
          </div>
          <div className="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm">
            <span className="text-sm font-medium text-stone-700">Blow Dry Style</span>
            <span className="text-sm font-bold text-[#2C2420]">+$35</span>
          </div>
        </div>
      </div>
    </section>
  );
}
