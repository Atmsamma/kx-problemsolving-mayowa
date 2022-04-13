import mongo from './mongo'
import userSchema from './user-schema'

const connectToMongoDB = async () => {
  await mongo().then(async (mongoose) => {
    try {
      console.log('Connected to mongodb!')

      const user = {
        email: 'test@email.com',
        username: 'Joe',
        password: 'Password1!',
      }

      await new userSchema(user).save()
    } finally {
      mongoose.connection.close()
    }
  })
}

connectToMongoDB()