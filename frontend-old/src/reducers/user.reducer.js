const initalState = { users:[], user:{}}
export const addUserAction = user => ({ type : "ADD_USER", payload:user})
export const deleteUserAction = userName => ({type:"DELETE_USER", payload: userName})
const userReducer = (state = initalState, action) => {
    switch(action.type){
        case 'ADD_USER' : return{ ...state, users: [ ...state.users, action.payload]}
        case 'DELETE_USER' : return {...state, users:state.users.filter(user => user.username !== action.payload)}
        default : return state
    }
}
export default userReducer