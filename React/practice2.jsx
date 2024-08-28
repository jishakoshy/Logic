//  useReducer 
import React from 'react';
import { useReducer } from "react";

function calculator() {
    const initialState = {result:0};
    const reducer = (state,action)=>{
        switch(action.type){
            case 'ADD':
                return {result: state.result + action.value}
            case 'SUB':
                return {result : state.result - action.value}
            case 'MUL':
                return {result :state.result * action.value}
            case 'DIV':
                return {}
        }
    }
    const [state, dispatch] = useRedcer(reducer,initialState);
    return(
        <div>
            <p>Calculator {}</p>
            <button>+</button>
            <button>-</button>
            <button>*</button>
            <button>/</button>
        </div>
    )
}
export default calculator;