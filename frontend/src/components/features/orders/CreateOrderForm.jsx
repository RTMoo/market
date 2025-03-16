import { useState } from 'react';
import FormInput from '../../commons/FormInput';
import { createOrder } from '../../../api/order';
import { useNavigate } from 'react-router-dom';


const CreateOrderForm = ({ totalPrice }) => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await createOrder(formData);
            if (response.status === 201) {
                navigate("/order")
            } else {
                console.log("Ошибка при создании заказа");
            }
        } catch (error) {
            console.error("Ошибка при создании заказа", error);
        }
    };

    return (
        <div className="bg-white rounded-lg p-4 shadow-md flex flex-col justify-between">
            <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
                <FormInput value={formData.fullName} name="full_name" label="ФИО" onChange={handleChange} />
                <FormInput value={formData.address} name="to_address" label="Адрес доставки" onChange={handleChange} />
                <FormInput value={formData.phone} name="phone_number" label="Номер телефона" onChange={handleChange} />
                <button type="submit" className="bg-blue-500 text-white p-2 rounded-lg">Оформить заказ</button>
            </form>

        </div>
    );
}


export default CreateOrderForm;
