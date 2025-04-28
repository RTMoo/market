import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const Paginator = ({ next, previous, current, total, onPageChange }) => {
    const getPages = () => {
        const pages = [];
        let start = Math.max(1, current - 2);
        let end = Math.min(total, start + 4);

        // Подправляем start, если мы в конце списка
        if (end - start < 4) {
            start = Math.max(1, end - 4);
        }

        for (let i = start; i <= end; i++) {
            pages.push(i);
        }

        return pages;
    };

    return (
        <div className="flex items-center space-x-2">
            <button
                onClick={() => onPageChange(current - 1)}
                disabled={!previous}
                className="px-3 py-1 border rounded disabled:opacity-50"
            >
                ← Назад
            </button>

            {getPages().map((page) => (
                <button
                    key={page}
                    onClick={() => onPageChange(page)}
                    className={`px-3 py-1 border rounded ${
                        current === page ? 'bg-black text-white' : ''
                    }`}
                >
                    {page}
                </button>
            ))}

            <button
                onClick={() => onPageChange(current + 1)}
                disabled={!next}
                className="px-3 py-1 border rounded disabled:opacity-50"
            >
                Вперед →
            </button>
        </div>
    );
};

export default Paginator;
