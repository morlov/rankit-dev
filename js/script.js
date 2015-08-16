$(document).ready(function()
{	
	// Sorting
	
	$(function() {
		$(".ranking-body").sortable({revert: 200, 
			update: function(event, ui) {
	        	var i = 1
	        	$(this).children(".ranking-item").each(function(idx, val){
					$(this).find(".item-rank").html(i++);
	            });	
			}
			});
		$(".ranking-body").sortable("disable");
		$(".ranking-body").disableSelection();
	});

	var cached_ranking_content = $(".ranking-body").html();

	$("#sort-ranking").click(function(){
		if($(this).val() === "Cancel") {
		  	$(".ranking-body").sortable("disable");
		  	$(this).val("Sort");
    		$(".ranking-body").html(cached_ranking_content).sortable("refresh");
		}
		else {
		 	$(".ranking-body").sortable("enable");
		  	$(this).val("Cancel");
		};
		$("#submit-ranking").toggle("slow", function(){});
	});
	
	// New ranking
	var i = 1;
	$("#add-item").on('click', function(){
		$(".ranking-body").sortable("enable");
		var item_name = $("#item-name").val();
		var item_content = $("#item-content").val();
		if(item_name != '') {
		 	var new_item =
		 		'<tr class="ranking-item">' +
		 			'<td class="item-rank">' + (i++) +'</td>' +
		 			'<td>' +
		 				'<span class="item-name">' + item_name + '</span>' +
		 				'<span class="glyphicon glyphicon-chevron-down open"></span>' +
					'</td>' +
		 		'</tr>' +
		 		'<tr class="item-content">' +
		 			'<td colspan="2">' + item_content + '</td>' +
		 		'</tr>';
			$(new_item).appendTo($(".ranking-body"));
			$("#item-name").val("");
			$("#item-content").val("");
		}      
	});

	$("#post-new-ranking").on('submit', function(event) {
		
		var ranking = {
			title: $("#ranking-title-input").val(),
			item_names: [],
			item_contents: []
		};

		if(ranking.title === '') { 
			alert('Please enter title of ranking!'); 
			return false; 
		}
		
		$(".ranking-body").children(".ranking-item").each(function(idx, val){
			ranking.item_names.push($(this).find(".item-name").text());
        });
		
		$(".ranking-body").children(".item-content").each(function(idx, val){
			ranking.item_contents.push($(this).text());
        });

		if(ranking.item_names.length < 2) { 
			alert('You should at least two items!' + ranking.item_names.length ); 
			return false; 
		}
		$("input[name='ranking']").val(JSON.stringify(ranking));
		$("#submit-ranking").attr("disabled","disabled");
	});
	
	// Update and post
	
	$("#post-ranking").submit(function(event) {
		var ranking = {
		item_ids: [],
		};
		$(".ranking-body").children().each(function(idx, val){
			ranking.item_ids.push($(this).data("item-id"));
        });	
		$("input[name='ranking']").val(JSON.stringify(ranking));
		$("#submit-ranking").attr("disabled","disabled");
	});

	//	Ranking displaying content
	
	$(".ranking-body").on('click', ".open", 
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

	$(".ranking-body").on('mouseenter', ".ranking-item",
		function() {
		$(this).find(".open").show();
	});

	$(".ranking-body").on('mouseleave', ".ranking-item",
	 	function() { 
	 	$(this).find(".open").hide();
	});

});