import React from "react";
import { useSelector } from 'react-redux'

export default function TodoList(){
    const todos = useSelector(state => state.todoReducer.todos)
    return(
        <div style={{textAlign:'center'}}>
            {todos.length === 0 && (<h1 >등록된 할 일 목록이 없습니다.</h1>)}
        {todos.length !== 0 && (<h1>{todos.length}개의 할 일 목록이 있습니다.</h1>)}
        </div>
    )
}