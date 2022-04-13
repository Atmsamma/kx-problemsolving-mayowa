import { Schema, model } from 'mongoose'

const reqString = {
  type: String,
  required: true,
}

const userSchema = Schema({
  email: reqString,
  username: reqString,
  password: reqString,
})

export default model('users', userSchema)