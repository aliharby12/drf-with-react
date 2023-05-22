import React from 'react';
import InvoiceList from './InvoiceList';
import CreateInvoiceForm from './CreateInvoiceForm';

const App = () => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <div style={{ marginRight: '100px' }}>
        <InvoiceList />
      </div>
      <div>
        <CreateInvoiceForm />
      </div>
    </div>
  );
};

export default App;
