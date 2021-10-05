import React, { useState } from 'react';
import { useDispatch } from 'react-redux'
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { addUserAction } from 'reducers/user.reducer';
import { userRegister } from 'api';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();

export default function UserJoin() {
    
    const [ user, setUser ] = useState({
      username : '',
      name : '',
      email : '',
      password : '',
      birth : '',
      address : ''
    })
    
    const { username, name, email, password, birth, address } = `user`
    // const [ birth, setBirth ] = useState('')
    // const [ address, setAddress ] = useState('')
    // const [ email, setEmail ] = useState('')
    // const [ password, setPassword] = useState('')
    // 각각 만들지 않고 통합해서 만들기 가능 - AOP
    const dispatch = useDispatch()

    const submitForm = (e) => {
        e.preventDefault();
        alert(`가입 회원 정보: ${JSON.stringify(user)}`)
        addUser(user)
        userRegister({user})
        .then(res => {alert(`회원가입 완료 : ${res.data.result}`)})
        .catch(err => {alert(`회원가입 실패 : ${err}`)})
    }    
    const addUser = payload => dispatch(addUserAction(payload))


    const handleChange =e => {
      e.preventDefault()
      const { name, value } = e.target
      // alert(`name: ${name}, value: ${value}`)
      setUser ({
        ...user,
        [name] : value
      })
    }

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Join
          </Typography>
          <Box component="form" onSubmit={submitForm} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="user name"
              name="username"
              autoComplete="username"
              value={username}
              onChange={handleChange}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="name"
              label="name"
              name="name"
              autoComplete="name"
              value={name}
              onChange={handleChange}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              value={password}
              onChange={handleChange}
              autoComplete="current-password"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              value={email}
              onChange={handleChange}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="birth"
              label="user birth"
              name="birth"
              autoComplete="birth"
              value={birth}
              onChange={handleChange}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="address"
              label="user Address"
              name="address"
              autoComplete="Address"
              value={address}
              onChange={handleChange}
              autoFocus
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Button
              type="button"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              취소
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}