import React, { useState } from 'react'

function practice() {
    const [count, setCount] = useState('')
    // const Increment = ()=>{
    //     setCount(count+1)
    // }
    // const Decrement = ()=>{
    //     setCount(count-1)
    // }
    return(
        <div>
            <p>Click {count}</p>
            <button onClick ={()=> setCount(count + 1)}>Increment  </button>
            <button onClick={()=> setCount(count-1)}>Decrement</button>
        </div>
    )
}
export default practice