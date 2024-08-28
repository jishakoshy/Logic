import React, { useEffect, useState } from 'react'

function first() {

    const [count,setcount] = useState(0);
    useEffect(()=>{
        console.log("mount")
        return()=>{
            console.log("unmount")
        }
    },[count])
    return(
        <div>
            <p>{count}</p>
            <button onClick={()=>setcount(count+1)}>increment</button>
        </div>
    )
}
export default first


// import React from 'react'

// function first() {
//   return (
//     <div>first</div>
//   )
// }

// export default first