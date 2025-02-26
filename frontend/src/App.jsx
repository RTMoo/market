import { useState } from 'react'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='w-full flex justify-center flex-col'>
        <button className='m-auto px-5 py-3 bg-blue-300 w-32' onClick={() => setCount(count + 1)}>inc</button>
        <div className='m-auto'>{count}</div>
      </div>
    </>
  )
}

export default App
