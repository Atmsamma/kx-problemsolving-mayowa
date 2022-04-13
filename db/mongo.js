import mongoose, { connect } from 'mongoose'
const mongoURl = "mongodb://" + process.env.MONGO_INITDB_ROOT_USERNAME +  ":" + process.env.MONGO_INITDB_ROOT_PASSWORD + "@" + process.env.MONGODB_ADVERTISED_HOSTNAME + "27017/" + process.env.MONGO_INITDB_DATABASE

export default async () => {
  await connect(mongoURl, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })

  return mongoose
}