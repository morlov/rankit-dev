$(document).ready(function()
{	
	
	// Sorting
	$(function() {
		$(".ranking").sortable({revert: 200,
			items: ".item-body",
			update: function(event, ui) {
	        	var i = 1
	        	$(this).children(".item-body").each(function(idx, val){
					$(this).find(".item-rank").html(i++);
	            });	
			}
			});
		$(".ranking").sortable("disable");
		$(".ranking").disableSelection();
	});

	var sortableCache = $(".ranking").html();

	$("#sort-ranking").click(function(){
		if($(this).html() === "Cancel") {
		  	$(".ranking").sortable("disable");
		  	$(this).html("Sort");
		  	$('.ranking').html(sortableCache).sortable("refresh");
		}
		else {
		 	$(".ranking").sortable("enable");
		  	$(this).html("Cancel");
		};
		$("#submit-ranking").toggle("slow", function(){});
	});

	
	// New ranking
	var i = 1;
	$("#add-item").on('click', function(){
		var itemName = $("#item-name").val();
		var itemContent = $("#item-content").val();
		if(itemName != '') {
		 	var newItem =
		 		'<tbody class="item-body">' +
		 			'<tr class="ranking-item">' +
		 				'<td class="item-rank">' + (i++) +'</td>' +
		 				'<td>' +
		 					'<span class="item-name">' + itemName + '</span>' +
		 					'<span class="glyphicon glyphicon-chevron-down open"></span>' +
		 				'</td>' +
		 			'</tr>' +
		 			'<tr class="item-content">' +
		 				'<td colspan="2">' + itemContent + '</td>' +
		 			'</tr>' +
		 		'</tbody>';
		 	$(newItem).appendTo($(".ranking"));
			$("#item-name").val("");
			$("#item-content").val("");
		}
		if ($(".ranking").children(".item-body").length >= 2) {
			$(".ranking").sortable("enable");
			$("#submit-ranking").removeAttr('disabled');
		}
	});

	$("#post-new-ranking").on('submit', function(event) {
		
		var ranking = {
			title: $("#ranking-title-input").val(),
			itemNames: [],
			itemContents: []
		};

		if(ranking.title === '') { 
			alert('Please enter title of ranking!'); 
			return false; 
		}
		
		$(".ranking").children(".item-body").each(function(idx, val){
			ranking.itemNames.push($(this).find(".item-name").text());
			ranking.itemContents.push($(this).find(".item-content").text());
        });

		if(ranking.itemNames.length < 2) { 
			alert('You should at least two items! Got' + ranking.item_names.length ); 
			return false; 
		}
		$("input[name='ranking']").val(JSON.stringify(ranking));
		$("#submit-ranking").attr("disabled","disabled");
	});
	
	// Update and post
	
	$("#post-ranking").submit(function(event) {
		var ranking = {
			ranks: [],
		};
		$(".ranking").children(".item-body").each(function(idx, val){
			ranking.ranks.push($(this).data("item-rank"));
        });	
		$("input[name='ranking']").val(JSON.stringify(ranking));
		$("#submit-ranking").attr("disabled","disabled");
	});

	//	Ranking displaying content
	
	$(".ranking-panel").on('click', ".open", 
		function() {
			$(this).closest(".ranking-item").next().slideToggle();
			if($(this).val()==="show") {
				$(this).val("hide");
				$(this).attr("class", "glyphicon glyphicon-chevron-down open");
			}
			else {
				$(this).val("show");
				$(this).attr("class", "glyphicon glyphicon-chevron-up open");
			}
	});

	$(".ranking-panel").on('mouseenter', ".ranking-item",
		function() {
		$(this).find(".open").show();
	});

	$(".ranking-panel").on('mouseleave', ".ranking-item",
	 	function() { 
	 	$(this).find(".open").hide();
	});

});