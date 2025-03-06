const FormInput = ({ label, type = "text", name, value, onChange, disabled = false, isTextArea = false }) => {
    return (
        <div className="w-full">
            <label className="block text-gray-600">{label}</label>

            {isTextArea ? (
                <textarea
                    name={name}
                    value={value}
                    onChange={onChange}
                    disabled={disabled}
                    className="w-full p-2 border border-gray-300 rounded-lg focus:ring-blue-500 resize-y min-h-[100px]"
                />
            ) : (
                <input
                    type={type}
                    name={name}
                    value={value}
                    onChange={onChange}
                    disabled={disabled}
                    className="w-full p-2 border border-gray-300 rounded-lg focus:ring-blue-500"
                />
            )}
        </div>
    );
};



export default FormInput;
