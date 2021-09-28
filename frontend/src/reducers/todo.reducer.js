const initialState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type : "ADD_TODO", payload: todo})
const todoReducer = (state = initialState, aciton) => {
    switch(aciton.type){
        default : return state
    }
}
export default todoReducer