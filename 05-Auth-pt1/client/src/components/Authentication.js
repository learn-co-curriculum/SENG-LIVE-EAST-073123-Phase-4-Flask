import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'
import styled from "styled-components";
import { useFormik } from "formik"
import * as yup from "yup"

function Authentication({updateUser}) {
  const [signUp, setSignUp] = useState(false)
  const history = useHistory()

  const handleClick = () => setSignUp((signUp) => !signUp)
    //build the authentication form with formik

    const formSchema = yup.object().shape({ 
      // use yup to make some client side validations
      name: yup.string().required("Enter a username"),
      email: yup.string().email()
    })
    
    const formik = useFormik({ 
      //Formik handles the value, onchange 
      //and onsubmit events of the form in JSX
      initialValues:{
        name: '',
        email: ''
      },
      validationSchema: formSchema,
    
      //in formik, on submit to create a POST. 
      onSubmit:(values) => {
            fetch(signUp? '/users': '/login', { //toggles btw login/sign up
              method: "POST", //if signing up-> POST request w 'users' route
              headers:{
                "Content-Type": "application/json"
              },
              body: JSON.stringify(values, null, 2)
            })
            .then(resp => resp.json())
            .then(user => {
              updateUser(user) //(updateUser is passed down from app through props)
              history.push('/') //redirect to the Home page.
              console.log("hello")
              //successful POST add the user to state 
            })
          },
      })
      
      console.log("sign up? (or login?) ---- ", signUp)
    //react handle the submit and change by 
    //controlled form using "FORMIK"
    return (
      <> 
        <h2 style={{color:'red'}}> {formik.errors.name}</h2>
        <h2>Please Log in or Sign up!</h2>
        <h2>{signUp?'Already a member?':'Not a member?'}</h2>
        <button onClick={handleClick}>{signUp?'Log In!':'Register now!'}</button>
        <Form onSubmit={formik.handleSubmit}>
            <label>
              Username
            </label>
            
            <input type='text' 
                  name='name' 
                  value={formik.values.name} 
                  onChange={formik.handleChange} />

            {signUp&&(
              <>
                  <label>
                    Email
                  </label>
                  <input type='text' 
                        name='email' 
                        value={formik.values.email} 
                        onChange={formik.handleChange} />
              </>
            )}

            <input type='submit' 
                   value={signUp?'Sign Up!':'Log In!'} />
        </Form>
      </>
    )
}

export default Authentication

export const Form = styled.form`
display:flex;
flex-direction:column;
width: 400px;
margin:auto;
font-family:Arial;
font-size:30px;
input[type=submit]{
  background-color:#42ddf5;
  color: white;
  height:40px;
  font-family:Arial;
  font-size:30px;
  margin-top:10px;
  margin-bottom:10px;
}
`