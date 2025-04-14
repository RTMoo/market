import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { confirmCode } from '../../api/auth';

const ConfirmCode = () => {
    const navigate = useNavigate();
    const email = localStorage.getItem("confirmEmail");
    const [code, setCode] = useState(['', '', '', '', '', '']);

    const handleChange = (e, index) => {
        const val = e.target.value.replace(/\D/g, ''); // только цифры
        if (!val) return;

        const newCode = [...code];
        newCode[index] = val[0];
        setCode(newCode);

        // вставка нескольких символов (например из буфера обмена)
        if (val.length > 1) {
            const chars = val.split('');
            for (let i = 0; i < chars.length && index + i < 6; i++) {
                newCode[index + i] = chars[i];
            }
            setCode(newCode);
            const nextIndex = Math.min(index + chars.length, 5);
            document.getElementById(`code-input-${nextIndex}`).focus();
        } else if (index < 5) {
            document.getElementById(`code-input-${index + 1}`).focus();
        }
    };

    const handleKeyDown = (e, index) => {
        if (e.key === 'Backspace') {
            e.preventDefault();
            const newCode = [...code];
            if (code[index]) {
                newCode[index] = '';
                setCode(newCode);
            } else if (index > 0) {
                newCode[index - 1] = '';
                setCode(newCode);
                document.getElementById(`code-input-${index - 1}`).focus();
            }
        } else if (e.key === 'ArrowLeft' && index > 0) {
            document.getElementById(`code-input-${index - 1}`).focus();
        } else if (e.key === 'ArrowRight' && index < 5) {
            document.getElementById(`code-input-${index + 1}`).focus();
        }
    };

    const handleSubmit = async () => {
        const data = { code: code.join(''), email: email };
        try {
            const response = await confirmCode(data);
            if (response.status === 200) {
                navigate("/login");
            }
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="flex justify-center items-center h-screen">
            <div className="text-center">
                <h2 className="text-2xl font-semibold mb-4">Введите код подтверждения</h2>
                <div className="flex justify-between gap-2 mb-4">
                    {code.map((digit, index) => (
                        <input
                            key={index}
                            id={`code-input-${index}`}
                            type="text"
                            inputMode="numeric"
                            value={digit}
                            onChange={(e) => handleChange(e, index)}
                            onKeyDown={(e) => handleKeyDown(e, index)}
                            maxLength={1}
                            className="w-12 h-12 text-2xl text-center border-2 border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                    ))}
                </div>
                <button
                    onClick={handleSubmit}
                    className="px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                >
                    Подтвердить
                </button>
            </div>
        </div>
    );
};

export default ConfirmCode;
