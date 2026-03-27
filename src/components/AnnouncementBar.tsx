import { MapPin, Clock } from 'lucide-react';

export function AnnouncementBar() {
  return (
    <div className="bg-[#2C2420] text-stone-300 py-3 relative z-50">
      <div className="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row justify-between items-center gap-2 text-[10px] sm:text-[11px] uppercase tracking-wider font-medium">
        <span className="opacity-90 flex items-center gap-2">
          <span className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
          Grand Opening Special: 20% Off First Visit
        </span>
        <div className="flex items-center gap-6">
          <span className="flex items-center gap-1.5 hover:text-white cursor-pointer transition-colors">
            <MapPin className="w-3 h-3" /> 123 Wellness Blvd, Los Angeles
          </span>
          <span className="flex items-center gap-1.5">
            <Clock className="w-3 h-3" /> Daily 10am - 8pm
          </span>
        </div>
      </div>
    </div>
  );
}
