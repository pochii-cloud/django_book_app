const draggable=document.querySelectorAll('.draggable')
const containers= document.querySelectorAll('.container')

 draggable.forEach(draggable => {
     draggable.addEventListener('dragstart', () => {
         draggable.classList.add('dragging')
     })
     draggable.addEventListener('dragend', () => {
         draggable.classList.remove('dragging')
     })
 })
containers.forEach(container =>{
    container.addEventListener('dragover',e  =>{
        e.preventDefault()
        const afterElement =getDragAfterElement(container,e.clientY)
         const draggable =document.querySelector('.dragging')
        if (afterElement == null){
             container.appendChild(draggable)
        }
        else {
            container.insertBefore(draggable,afterElement)
        }
    })
})
function  getDragAfterElement(container ,y){
   const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')]
    draggableElements.reduce((closest,child) =>{
       const box=child.getBoundingClientRect()
        const offset = y-box.top -box.height / 2
        console.log(box)
        if (offset <0 && offset > closest.offset){
            return {offset:offset,element:child}
        }
        else {
            return closest
        }
    },{offset:Number.NEGATIVE_INFINITY})
}