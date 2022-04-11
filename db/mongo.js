const mongoose = require('mongoose')
const mongoURl = `mongodb://root:password@localhost:27017/flaskdb`

module.exports = async () => {
  await mongoose.connect(mongoURl, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })

  return mongoose
}