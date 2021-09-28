import React, {useState} from "react";
import { useDispatch } from 'react-redux'
import { v4 as uuid4 } from 'uuid'

export default function Todo(){

    const [todo, setTodo] = useState('')

    const submitForm = e => {
        e.preventDefault()
        const newTodo = {
            id : uuid4(),
            name : todo,
            complete : false
        }
        addTodo(newTodo)
        setTodo('')
    }

    const addTodo = todo => dispatchEvent(addTodoAction)

    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }

    return (
    <form onSubmit={submitForm} method='POST'>
    <div style={{textAlign:'center', marginTop:'150px'}}>
        <input type='text' 
                id='todo'
                name = 'todo'
                placeholder = '할 일 입력'
                value = {todo}
                onChange={handleChange} />
        <input type='submit'
                value='ADD'/><br/>
    </div></form>)
}