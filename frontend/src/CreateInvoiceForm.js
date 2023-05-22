import React, { useState } from 'react';
import axios from 'axios';

const CreateInvoiceForm = () => {
    const [invoiceData, setInvoiceData] = useState({
        group: '',
        description: '',
        price: 0.0,
        qnty: 0,
        item_name: '',
    });
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleInputChange = (event) => {
        const { name, value } = event.target;

        if (name === 'price') {
            setInvoiceData({
                ...invoiceData,
                [name]: parseFloat(value),
            });
        } else if (name === 'qnty') {
            setInvoiceData({
                ...invoiceData,
                [name]: parseInt(value),
            });
        } else {
            setInvoiceData({
                ...invoiceData,
                [name]: value,
            });
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/invoice/create-invoice/', invoiceData);
            console.log('Invoice created successfully:', response.data);
            setSuccessMessage('Invoice created successfully.');
            setErrorMessage('');
            // Reset the form or perform any necessary actions after successful submission
        } catch (error) {
            console.error('Error creating invoice:', error.response.data);
            setErrorMessage('An error occurred while creating the invoice.');
            setSuccessMessage('');
            // Handle any error states or display error messages
        }
    };

    return (
        <div>
            <h2>Create Invoice</h2>
            {successMessage && <p>{successMessage}</p>}
            {errorMessage && <p>{errorMessage}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Invoice Group:</label>
                    <input
                        type="number"
                        name="group"
                        value={invoiceData.group}
                        onChange={handleInputChange}
                        style={{ marginBottom: '10px' }}
                    />
                </div>
                <div>
                    <label>Description:</label>
                    <textarea
                        name="description"
                        value={invoiceData.description}
                        onChange={handleInputChange}
                        style={{ marginBottom: '10px' }}
                    />
                </div>
                <div>
                    <label>Item Name:</label>
                    <textarea
                        name="item_name"
                        value={invoiceData.item_name}
                        onChange={handleInputChange}
                        style={{ marginBottom: '10px' }}
                    />
                </div>
                <div>
                    <label>Price:</label>
                    <input
                        type="number"
                        name="price"
                        step="0.01"
                        value={invoiceData.price}
                        onChange={handleInputChange}
                        style={{ marginBottom: '10px' }}
                    />
                </div>
                <div>
                    <label>Quantity:</label>
                    <input
                        type="number"
                        name="qnty"
                        value={invoiceData.qnty}
                        onChange={handleInputChange}
                        style={{ marginBottom: '10px' }}
                    />
                </div>
                <button type="submit" style={{ marginTop: '10px' }}>
                    Create Invoice
                </button>
            </form>
        </div>
    );
};

export default CreateInvoiceForm;
