import { CalendarDays } from 'lucide-react';

export function FloatingButton() {
  return (
    <div className="fixed bottom-6 right-6 z-50 md:hidden">
      <button className="bg-[#2C2420] text-white p-4 rounded-full shadow-2xl hover:scale-105 transition-transform">
        <CalendarDays className="w-6 h-6" />
      </button>
    </div>
  );
}
