const initialState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type : "ADD_TODO", payload: todo})
const todoReducer = (state = initialState, aciton) => {
    switch(aciton.type){
        case 'ADD_TODO' : return {...state, todos: [...state.todos, aciton.payload]}
        default : return state
    }
}
export default todoReducer