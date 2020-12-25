const express = require('express');
const router = express.Router()

router.get('/', (req, res) => {

})

router.get('/posts', (req, res) => {

})

router.get("/:teste", (req, res) => {
    res.status(200).json({teste: "oi"})
});


module.exports = router;