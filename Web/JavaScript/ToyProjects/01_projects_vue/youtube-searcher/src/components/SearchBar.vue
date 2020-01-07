<template>
  <div>
    <input @change="onInput" type="text">
  </div>
</template>

<script>

export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      this.$emit('inputChange', event.target.value)
    }
  }
}
</script>

<style>

</style>