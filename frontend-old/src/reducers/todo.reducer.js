const initialState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type : "ADD_TODO", payload: todo})
export const toggleTodoAciton = todoId => ({type:"TOGGLE_TODO", payload: todoId})
export const deleteTodoAction = todoId => ({type:"DELETE_TODO", payload: todoId})
const todoReducer = (state = initialState, aciton) => {
    switch(aciton.type){
        case 'ADD_TODO' : return {...state, todos: [...state.todos, aciton.payload]}
        case 'TOGGLE_TODO' : return {...state, todos: state.todos.map(todo => (todo.id === aciton.payload)
                                                                          ? {...todo, complete: !todo.complete} : todo )}
        case 'DELETE_TODO' : return {...state, todos:state.todos.filter(todo => todo.id !== aciton.payload)}
        default : return state
    }
}
export default todoReducer