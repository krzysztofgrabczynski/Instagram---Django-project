document.querySelector('#element').addEventListener('mouseover', function () {
	document.querySelector('#additional-content').style.display = 'block';
});

document.querySelector('#element').addEventListener('mouseout', function () {
	document.querySelector('#additional-content').style.display = 'none';
});