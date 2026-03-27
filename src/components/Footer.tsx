import { Flower2, Instagram, Facebook, Youtube, MapPin, Phone, Mail } from 'lucide-react';

export function Footer() {
  return (
    <footer className="bg-[#1C1917] text-stone-400 pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid md:grid-cols-4 gap-12 border-b border-white/10 pb-12">
          <div className="col-span-1 md:col-span-2 space-y-6">
            <a href="#" className="flex items-center gap-2 text-white">
              <Flower2 className="w-6 h-6" />
              <span className="text-xl font-bold tracking-tight">Calm & Cozy.</span>
            </a>
            <p className="text-sm leading-relaxed max-w-sm">
              Los Angeles' premier destination for authentic Korean Head Spa therapy. We believe in the harmony of scalp health and mental well-being.
            </p>
            <div className="flex gap-4 pt-2">
              <a href="#" className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/20 transition-colors"><Instagram className="w-4 h-4 text-white" /></a>
              <a href="#" className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/20 transition-colors"><Facebook className="w-4 h-4 text-white" /></a>
              <a href="#" className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/20 transition-colors"><Youtube className="w-4 h-4 text-white" /></a>
            </div>
          </div>

          <div>
            <h4 className="text-white font-bold uppercase text-xs tracking-widest mb-6">Contact</h4>
            <ul className="space-y-4 text-sm">
              <li className="flex items-start gap-3">
                <MapPin className="w-4 h-4 mt-0.5 text-stone-500" />
                <span>123 Wellness Blvd, Suite 100<br />Los Angeles, CA 90210</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone className="w-4 h-4 text-stone-500" />
                <span>(555) 123-4567</span>
              </li>
              <li className="flex items-center gap-3">
                <Mail className="w-4 h-4 text-stone-500" />
                <span>hello@calmandcozy.com</span>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-white font-bold uppercase text-xs tracking-widest mb-6">Hours</h4>
            <ul className="space-y-2 text-sm">
              <li className="flex justify-between">
                <span>Monday - Friday</span>
                <span className="text-white">10am - 8pm</span>
              </li>
              <li className="flex justify-between">
                <span>Saturday</span>
                <span className="text-white">9am - 7pm</span>
              </li>
              <li className="flex justify-between">
                <span>Sunday</span>
                <span className="text-white">10am - 6pm</span>
              </li>
            </ul>
          </div>
        </div>
        
        <div className="pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-stone-500">
          <p>&copy; 2024 Calm & Cozy Spa. All Rights Reserved.</p>
          <div className="flex gap-6">
            <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
