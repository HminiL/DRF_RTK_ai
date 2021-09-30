import React from "react";
import { useSelector,useDispatch } from 'react-redux'
import { deleteUserAction } from 'reducers/user.reducer'

export default function UserList(){
    const users = useSelector( state => state.userReducer.users)
    const dispatch = useDispatch()
    const deleteUser = email => dispatch(deleteUserAction(email))
    return(<>
        <div style={{textAlign:'center'}}>
            {users.length === 0 && <h1>등록된 회원이 없습니다.</h1>}
            {users.length !== 0 && <h1>{users.length}명의 등록된 회원이 있습니다.</h1>}
            {users.length !== 0 && users.map(
                user => (<div key={user.name}>
                    {user.username.length === 0 ?
                    <span >null</span>
                    : <span>{user.username}</span>}
                <button onClick={deleteUser.bind(null, user.username)}>X</button>
                </div>))}
        </div>
    </>)
}