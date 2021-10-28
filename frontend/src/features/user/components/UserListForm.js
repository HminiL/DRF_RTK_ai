import React from 'react'

const UserListForm = ({list}) => {
    return (<table border='1px' style={{textAlign:'center'}}>
    <thead>
    <tr><th>사용자번호</th>
        <th>사용자아이디</th>
        <th>이름</th>
        <th>이메일</th>
        <th>생년월일</th>
        <th>주소</th>
        
        </tr>
    </thead>
    <tbody>
    {list.map((user)=>(
        <tr><td>{user.userId}</td>
        <td>{user.username}</td>
        <td>{user.name}</td>
        <td>{user.email}</td>
        <td>{user.birth}</td>
        <td>{user.address}</td>
        </tr>
    ))}
    </tbody>
    </table>)
}

export default UserListForm