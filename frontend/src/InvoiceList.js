import React, { useEffect, useState } from 'react';
import axios from 'axios';

const InvoiceList = () => {
  const [invoices, setInvoices] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchInvoices();
  }, []);

  const fetchInvoices = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/invoice/all-invoices/', {
        params: {
          search: searchQuery
        }
      });
      setInvoices(response.data.results.slice(0, 3));
    } catch (error) {
      console.error('Error fetching invoices:', error);
    }
  };

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    fetchInvoices();
  };

  return (
    <div>
      <h2>Invoices:</h2>
      <form onSubmit={handleSearchSubmit}>
        <input type="text" value={searchQuery} onChange={handleSearchChange} placeholder="search" />
        <button type="submit">Search</button>
      </form>
      {invoices.length > 0 ? (
        invoices.map((invoice) => (
          <div key={invoice.uuid}>
            <p>Group Title: {invoice.group.title}</p>
            <p>Invoice Number: {invoice.invoice_number}</p>
            <p>Description: {invoice.description}</p>
            <p>Item Name: {invoice.item_name}</p>
            <p>Price: {invoice.price} EGP</p>
            <hr />
          </div>
        ))
      ) : (
        <p>No invoices found</p>
      )}
    </div>
  );
};

export default InvoiceList;
