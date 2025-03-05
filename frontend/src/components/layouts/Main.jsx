import React from 'react';

const Main = ({ children }) => {
    return (
        <main className='w-full justify-center min-h-screen'>
            {children}
        </main>
    );
}

export default Main;
