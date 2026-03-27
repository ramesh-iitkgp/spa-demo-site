export function Team() {
  return (
    <section id="team" className="py-24 bg-stone-50">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-end mb-12">
          <div className="space-y-4">
            <span className="text-[#2C2420] text-xs font-bold tracking-widest uppercase">The Experts</span>
            <h2 className="text-4xl font-medium text-stone-900 tracking-tight">Meet Your Therapists</h2>
          </div>
          <a href="#" className="text-sm font-medium underline decoration-stone-300 underline-offset-4 hover:text-[#2C2420] transition-colors">See all staff</a>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {/* Team Member 1 */}
          <div className="group">
            <div className="aspect-[3/4] rounded-2xl overflow-hidden mb-6 relative">
              <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1976&auto=format&fit=crop" className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 group-hover:scale-105" alt="Therapist" />
              <div className="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-md p-4 rounded-xl translate-y-full group-hover:translate-y-0 transition-transform duration-300 opacity-0 group-hover:opacity-100">
                <p className="text-xs text-stone-500 leading-snug">"I specialize in tension relief and promoting scalp circulation for hair growth."</p>
              </div>
            </div>
            <h3 className="text-lg font-bold text-stone-900">Ji-Min Kim</h3>
            <p className="text-xs uppercase tracking-wider text-stone-500 mt-1">Head Therapist • 10 Years Exp</p>
          </div>

          {/* Team Member 2 */}
          <div className="group">
            <div className="aspect-[3/4] rounded-2xl overflow-hidden mb-6 relative">
              <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=1961&auto=format&fit=crop" className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 group-hover:scale-105" alt="Therapist" />
              <div className="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-md p-4 rounded-xl translate-y-full group-hover:translate-y-0 transition-transform duration-300 opacity-0 group-hover:opacity-100">
                <p className="text-xs text-stone-500 leading-snug">"My focus is on holistic relaxation, blending traditional techniques with modern care."</p>
              </div>
            </div>
            <h3 className="text-lg font-bold text-stone-900">Sarah Lee</h3>
            <p className="text-xs uppercase tracking-wider text-stone-500 mt-1">Scalp Specialist</p>
          </div>

          {/* Team Member 3 */}
          <div className="group">
            <div className="aspect-[3/4] rounded-2xl overflow-hidden mb-6 relative">
              <img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=1974&auto=format&fit=crop" className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 group-hover:scale-105" alt="Therapist" />
              <div className="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-md p-4 rounded-xl translate-y-full group-hover:translate-y-0 transition-transform duration-300 opacity-0 group-hover:opacity-100">
                <p className="text-xs text-stone-500 leading-snug">"Expert in neck and shoulder massage integration for complete stress relief."</p>
              </div>
            </div>
            <h3 className="text-lg font-bold text-stone-900">David Park</h3>
            <p className="text-xs uppercase tracking-wider text-stone-500 mt-1">Massage Therapist</p>
          </div>
        </div>
      </div>
    </section>
  );
}
