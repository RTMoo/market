import React from 'react';

const Main = ({ children }) => {
    return (
        <main className='h-screen w-full justify-center flex'>
            {children}
        </main>
    );
}

export default Main;
