import { ChevronDown } from 'lucide-react';

export function FAQ() {
  return (
    <section className="py-24 max-w-3xl mx-auto px-6">
      <h2 className="text-3xl font-medium text-stone-900 tracking-tight mb-10 text-center">Frequently Asked Questions</h2>
      <div className="space-y-4">
        {/* Item 1 */}
        <details className="group bg-white rounded-xl border border-stone-200 p-5 [&_summary::-webkit-details-marker]:hidden">
          <summary className="flex cursor-pointer items-center justify-between text-stone-900 font-semibold">
            Do I need to wash my hair before?
            <span className="ml-4 shrink-0 transition-transform group-open:rotate-180"><ChevronDown className="w-5 h-5 text-stone-400" /></span>
          </summary>
          <div className="mt-4 text-stone-600 text-sm leading-relaxed border-t border-stone-100 pt-4">
            No, please come as you are! Our treatment involves a deep cleanse and shampooing process, so there is no need to wash your hair beforehand.
          </div>
        </details>
        
        {/* Item 2 */}
        <details className="group bg-white rounded-xl border border-stone-200 p-5 [&_summary::-webkit-details-marker]:hidden">
          <summary className="flex cursor-pointer items-center justify-between text-stone-900 font-semibold">
            Is the Head Spa safe for extensions or colored hair?
            <span className="ml-4 shrink-0 transition-transform group-open:rotate-180"><ChevronDown className="w-5 h-5 text-stone-400" /></span>
          </summary>
          <div className="mt-4 text-stone-600 text-sm leading-relaxed border-t border-stone-100 pt-4">
            We do not recommend the full scaling treatment for tape-in or glued extensions as the steam and oils may loosen the adhesive. For colored hair, it is safe, but we suggest waiting 1 week after coloring.
          </div>
        </details>

        {/* Item 3 */}
        <details className="group bg-white rounded-xl border border-stone-200 p-5 [&_summary::-webkit-details-marker]:hidden">
          <summary className="flex cursor-pointer items-center justify-between text-stone-900 font-semibold">
            What happens during the Scalp Analysis?
            <span className="ml-4 shrink-0 transition-transform group-open:rotate-180"><ChevronDown className="w-5 h-5 text-stone-400" /></span>
          </summary>
          <div className="mt-4 text-stone-600 text-sm leading-relaxed border-t border-stone-100 pt-4">
            We use a high-definition trichology camera to view your scalp at 60x magnification. This allows us to see clogged pores, oil density, and sensitivity levels to customize your ampoule and shampoo selection.
          </div>
        </details>
      </div>
    </section>
  );
}
