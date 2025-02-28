
import React, { useEffect } from "react";

const Sidebar = ({ isOpen, toggleSidebar }) => {
    useEffect(() => {
        if (isOpen) {
            document.body.classList.add("overflow-hidden");
        } else {
            document.body.classList.remove("overflow-hidden");
        }

        return () => {
            document.body.classList.remove("overflow-hidden");
        };
    }, [isOpen]);
    return (
      <>
        {/* Затемнение фона */}
        <div
          className={`fixed inset-0 bg-[#00000020]  z-40 transition-opacity ${
            isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
          }`}
          onClick={toggleSidebar}
        />
        
        {/* Сайдбар */}
        <aside
          className={`fixed left-0 top-15 w-64 h-screen bg-gray-100 shadow-lg transition-transform duration-300 z-99 ${
            isOpen ? "translate-x-0" : "-translate-x-full"
          }`}
        >
          <ul className="p-4 overflow-y-auto h-full">
            <li className="p-2 hover:bg-gray-300">Категория 1</li>
            <li className="p-2 hover:bg-gray-300">Категория 2</li>
            <li className="p-2 hover:bg-gray-300">Категория 3</li>
          </ul>
        </aside>
      </>
    );
  };
export default Sidebar;
